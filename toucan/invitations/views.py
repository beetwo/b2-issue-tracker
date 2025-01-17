from allauth.account.adapter import get_adapter
from allauth.account.views import SignupView
from braces.views import UserPassesTestMixin, AnonymousRequiredMixin
from contact_form.views import ContactFormView
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

from ..organisations.models import Organisation
from .forms import InviteUserForm, RequestAccessContactForm
from .models import ToucanInvitation, create_invitation_from_request
from .permissions import can_invite_to_org
from .settings import INVITATION_SESSION_KEY


class InvitationAcceptedView(AnonymousRequiredMixin, DetailView):

    slug_field = 'secret_key'
    slug_url_kwarg = 'secret_key'

    def get_queryset(self):
        return ToucanInvitation.active.all()

    def get_authenticated_redirect_url(self):
        messages.error(
            self.request,
            _('''
                You have tried to accept an invitation to Toucan but you are already logged in.
                Please log out first and then try again by visiting the link in the invitation email.
                Or just ignore the email. Your choice.
            ''')
        )
        return super().get_authenticated_redirect_url()

    def get(self, request, *args, **kwargs):
        invitation = self.get_object()

        # save the invitation key in the session
        request.session[INVITATION_SESSION_KEY] = invitation.secret_key
        # verify the email
        adapter = get_adapter(request)
        adapter.stash_verified_email(request, invitation.email)
        # add a message for the user
        messages.info(
            request,
            _(
                'You have been invited to join %(organisation)s on Toucan. Please continue with the signup process.' % {
                    'organisation': invitation.organisation.name
                }
            )
        )
        # and redirect to
        return HttpResponseRedirect(reverse('account_signup'))


class InvitedSignupView(SignupView):

    def get(self, request, *args, **kwargs):
        self.initial = {
            "invitation_key": request.session.get(INVITATION_SESSION_KEY, '')
        }
        return super().get(request, *args, **kwargs)


class InviteToOrgView(UserPassesTestMixin, FormView):
    form_class = InviteUserForm
    template_name = 'invitations/invite.html'

    def get_success_url(self):
        return reverse('invite_to_org', kwargs={'organisation_id': self.organisation.pk})

    def test_func(self, user):
        return can_invite_to_org(user, self.organisation)

    @cached_property
    def organisation(self):
        return get_object_or_404(
            Organisation,
            pk=self.kwargs.get('organisation_id')
        )

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'organisation': self.organisation,
            'open_invitations': ToucanInvitation.objects.filter(organisation=self.organisation)
        })
        return ctx

    def form_valid(self, form):
        email = form.cleaned_data['email']
        messages.success(
            self.request,
            _('An email was sent to %(email)s inviting him to join you on Toucan' % {'email': email})
        )
        invitation = create_invitation_from_request(self.request, email)
        return super().form_valid(form)



class RequestInvitationFormView(ContactFormView):

    template_name = 'invitations/request_access/contact_form.html'
    form_class = RequestAccessContactForm

    def get_success_url(self):
        return reverse('request_invitation_form_sent')
