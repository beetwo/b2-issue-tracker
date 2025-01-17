import PropTypes from "prop-types";
import React from "react";
import { connect } from "react-redux";
import UI from "../components/main";
import getFilteredIssues from "../issueSelector";

import {
  selectIssue,
  fetchIssues,
  setCoordinates,
  resetCoordinates,
  loadCurrentUserInformation
} from "../actions";

class IssueTrackerApp extends React.Component {
  componentDidMount() {
    this.props.loadCurrentUserInformation();
    this.props.fetchIssues();
  }

  render() {
    // console.log("urxn");
    return <UI {...this.props} />;
  }
}

IssueTrackerApp.propType = {
  fetchIssues: PropTypes.func.isRequired,
  setCoordinates: PropTypes.func.isRequired,
  issues: PropTypes.array.isRequired,
  coordinates: PropTypes.object,
  loadCurrentUserInformation: PropTypes.func.isRequired,
  bounds: PropTypes.array.isRequired,
  // Injected by React Router
  children: PropTypes.node
};

const mapStateToProps = state => {
  return {
    allIssues: state.redux_issues,
    issues: getFilteredIssues(
      state.redux_issues,
      state.issueFilters.selections
    ),
    geojson: state.geojson,
    selectedIssue: state.selectedIssue,
    bounds: state.currentUser.bbox,
    coordinates: state.coordinates
  };
};

const mapDispatchToProps = dispatch => {
  return {
    fetchIssues: () => {
      dispatch(fetchIssues());
    },
    setCoordinates: latLng => {
      dispatch(setCoordinates(latLng));
    },
    clearCoordinates: () => {
      dispatch(resetCoordinates());
    },
    selectIssue: issue_id => {
      dispatch(selectIssue(issue_id));
    },
    loadCurrentUserInformation: () => {
      dispatch(loadCurrentUserInformation());
    }
  };
};

const RootUI = connect(mapStateToProps, mapDispatchToProps)(IssueTrackerApp);

export default RootUI;
