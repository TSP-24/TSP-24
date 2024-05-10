import { Link } from "react-router-dom";
import Papa from "papaparse";
import jschardet from "jschardet";
import iconv from "iconv-lite";
import React, { useState } from "react";
import { Button, Upload } from "antd";
import { InboxOutlined } from "@ant-design/icons";
import { useSelector, useDispatch } from "react-redux";
import { setImportedData } from "../../store/modules/importedDataStore";
import { classifyColumnLabels } from "../../utils/scoreTypeClasscify";
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
        complete: function (results) {
          const res = results.data;
          if (res[res.length - 1] === "") {
            res.pop();
          }

          // Convert CSV data to JSON format
          const jsonData = res.slice(1).map((row) => {
            const obj = {};
            row.forEach((value, index) => {
              obj[columnLabels[index]] = value;
            });
            return obj;
          });

          dispatch(setImportedData(jsonData));
          console.log("importedData updated (JSON format):", importedData);
        },
      });
    };
  };

  const renderNextStep = () => {
    setNextStepVisible(true);
  };

  const handleNextStep = () => {
    console.log(importedData);
  };

  const uploadProps = {
    name: "file",
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
          <li>
            <Link to="/search">Search</Link>
          </li>
          <li>
            <Link to="/students">Students</Link>
          </li>
          <li>
            <Link to="/">Home</Link>
          </li>
        </ul>
      </div>
      <h1>Welcome!</h1>
      <br />
      <br />
      <p>
        Student progress tracker.
        <br />
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
  );
};

export default Home;
