import { Link } from "react-router-dom";
import React, { useState } from 'react';
import { Button, Upload } from 'antd';
import { InboxOutlined } from '@ant-design/icons';
import { useSelector, useDispatch } from 'react-redux';
import { setScores, setAssessments } from "../../store/modules/importedDataStore";


const { Dragger } = Upload;

const Home = () => {
  const [nextStepVisible, setNextStepVisible] = useState(false);
  const importedData = useSelector((state) => state.importedData);
  const dispatch = useDispatch();

  const parseUploadCSVData = (file, callback) => {
    const reader = new FileReader();
    reader.onload = () => {
      console.log('Sending CSV content to server...');
      fetch('http://localhost:8000/uploads', {
        method: 'POST',
        mode: 'cors',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ data: reader.result,
                               filename: file.name})
      })
      .then(response => response.json())
      .then(data => {
        const scores = JSON.parse(data.scores); // Parse the scores from the response
        const assessments = data.assessments;   // Parse the assessments from the response
        dispatch(setScores(scores));            // Dispatch setScores action with scores data
        dispatch(setAssessments(assessments));  // Dispatch setAssessments action with assessments data
        console.log('Assessments parsed (JSON format):', assessments);
        console.log('importedData updated (JSON format):', scores);
        if (callback) callback();
      })
      .catch(error => console.error('Error during fetch:', error));
    };
    reader.onerror = () => console.error('Error reading file:', reader.error);
    reader.readAsText(file);
  };

  const renderNextStep = () => {
    setNextStepVisible(true);
  }

  const handleNextStep = () => {
    console.log(importedData);
  }

  const uploadProps = {
    name: 'file',
    multiple: false,
    showUploadList: false,
    beforeUpload: (file) => {
      parseUploadCSVData(file, renderNextStep);
      return false;
    },
  };

  return (
    <div className="index">
      <title>Welcome Page</title>
      <link rel="stylesheet" href="../CSS/bar.css" />
      <link rel="stylesheet" href="../CSS/button.css" />
      <div>
        <ul>
          <li><Link to="/search">Search</Link></li>
          <li><Link to="/students">Students</Link></li>
          <li><Link to="/">Home</Link></li>
        </ul>
      </div>
      <h1>Welcome!</h1>
      <br />
      <br />
      <p>
        Student progress tracker.<br />
        All-in-one dashboard for tracking student engagement
      </p>
      <div>
        <Dragger {...uploadProps}>
          <p className="ant-upload-drag-icon">
            <InboxOutlined />
          </p>
          <p className="ant-upload-text">upload csv file</p>
        </Dragger>
        {nextStepVisible && (
          <Button type="primary" onClick={handleNextStep}>
            Next
          </Button>
        )}
      </div>
    </div>

  )
}

export default Home;