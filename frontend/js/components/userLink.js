import PropTypes from "prop-types";
import React from "react";
import { Link } from "react-router-dom";

class UserLink extends React.Component {
  render() {
    let { username, linkTo, className } = this.props;
    let linkText = this.props.children ? this.props.children : username;

    let link = linkTo
      ? <a
          className="userLink"
          href={linkTo}
          target="_blank"
          className={className}
        >
          {linkText}
        </a>
      : <Link className="userLink" to={`/detail/${username}`}>
          {linkText}
        </Link>;
    return link;
  }
}

UserLink.propTypes = {
  username: PropTypes.string.isRequired,
  linkTo: PropTypes.string
};

export default UserLink;
