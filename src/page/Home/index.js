import { Link } from "react-router-dom";
import Papa from "papaparse";
import jschardet from "jschardet";
import iconv from "iconv-lite";
import React, { useState } from 'react';
import { Button, Upload } from 'antd';
import { InboxOutlined } from '@ant-design/icons';
import { useSelector, useDispatch } from 'react-redux';
import { setImportedData } from "../../store/modules/importedDataStore";
import {classifyColumnLabels} from "../../utils/scoreTypeClasscify";
import { setScoreType } from "../../store/modules/scoreTypeStore";


const { Dragger } = Upload;

const Home = () => {
  const [nextStepVisible, setNextStepVisible] = useState(false);
  const importedData = useSelector((state) => state.importedData);
  const scoreType = useSelector((state) => state.scoreType);

  const dispatch = useDispatch();

  const parseUploadCSVData = (file, callback) => {
    const fReader = new FileReader();
    fReader.readAsBinaryString(file);
    fReader.onload = (event) => {
      let fileBuf = event.target.result;
      const encodeType = jschardet.detect(fileBuf).encoding;
  
      let textData;
      if (encodeType !== "UTF-8") {
        textData = iconv.decode(fileBuf, encodeType);
      } else {
        textData = fileBuf;
      }
  
      iconv.skipDecodeWarning = true;
  
      Papa.parse(file, {
        encoding: textData,
        complete: function(results) {
          const res = results.data;
          if (res[res.length - 1] === "") {
            res.pop();
          }
  
          // Use the first row as column labels
          const columnLabels = res[0];

          //classify quiz, assignment, exam, attendance
          const classifiedLabels = classifyColumnLabels(columnLabels);

          // dispatch(setScoreType(classifiedLabels.quiz));
          // dispatch(setScoreType(classifiedLabels.exam));
          // dispatch(setScoreType(classifiedLabels.assignment));
          // dispatch(setScoreType(classifiedLabels.attendance));
          dispatch(setScoreType(classifiedLabels));

          console.log("classifiedLabels",classifiedLabels)

          console.log("scoreType",scoreType); 
          const quizCount = Array.isArray(classifiedLabels.quiz) ? classifiedLabels.quiz.length : 0;
          const examCount = Array.isArray(classifiedLabels.exam) ? classifiedLabels.exam.length : 0;
          const assignmentCount = Array.isArray(classifiedLabels.assignment) ? classifiedLabels.assignment.length : 0;
          const attendanceCount = Array.isArray(classifiedLabels.attendance) ? classifiedLabels.attendance.length : 0;

          //Here we suppose a fixed weight for each category: total quiz-10%, total assignment-40%, total exam-40%, attendance-10%.
          //And in each category, we give even weights.
          //If one category of above not exists, we do not count it in totalWeight, and calculate others by same proportion.
          
          let totalWeight = 0;
          if(quizCount!==0){
            totalWeight+=0.1
          }
          if(examCount!==0){
            totalWeight+=0.4
          }
          if(assignmentCount!==0){
            totalWeight+=0.4
          }
          if(attendanceCount!==0){
            totalWeight+=0.1
          }

         
          // Convert CSV data to JSON format
          const jsonData = res.slice(1).map(row => {
            const obj = {};
            row.forEach((value, index) => {
              obj[columnLabels[index]] = value;
            });
            return obj;
          });
  
          dispatch(setImportedData(jsonData));
          console.log('importedData updated (JSON format):', importedData);

          //For every data column in category above, get the highest data in the column as the full mark.
          // 

      const quizScores = classifiedLabels.quiz;
      console.log("quizScores.type",quizScores.type)

      
      const maxScores = {};

      for (const quiz of quizScores) {
      let maxScore = -0.1;

      for (const data of importedData) {
        const quizName = "Quiz: "+quiz; 
        if (data.hasOwnProperty(quizName)) { 
        const value = Number(data[quizName]);
          if (value>maxScore){
            maxScore = value;
      }
  }
  }

  maxScores[quiz] = maxScore; 
}

console.log("maxScores of quizs:", maxScores);




    }});

      


    }
  }

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