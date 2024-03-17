import { Link } from "react-router-dom";
import FileSaver from 'file-saver';
import Papa from "papaparse";
import jschardet from "jschardet";
import iconv from "iconv-lite";
import encoding from "encoding";

import React, { useState } from 'react';
import { Button, Upload, notification } from 'antd';
import { InboxOutlined } from '@ant-design/icons';

const { Dragger } = Upload;

const Home = ()=>{
  const [nextStepVisible, setNextStepVisible] = useState(false);
  const [importedData, setImportedData] = useState([]); // importedData to store imported json data

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
  
          // Convert CSV data to JSON format
          const jsonData = res.slice(1).map(row => {
            const obj = {};
            row.forEach((value, index) => {
              obj[columnLabels[index]] = value;
            });
            return obj;
          });
  
          setImportedData(jsonData);
          console.log('importedData updated (JSON format):', jsonData);
        }
      });
    }
  }
    const renderNextStep = () => {
        setNextStepVisible(true);
      }
    
      const handleNextStep = () => {
        console.log('下一步操作');
        console.log("data",importedData);

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
    return(
        <div className="index">
        <title>Welcome Page</title>

        <link rel="stylesheet" href="../CSS/bar.css"/>
        <link rel="stylesheet" href="../CSS/button.css"/>

            <div>
            <ul>
                <li><Link to="/search">Search</Link></li>
                <li><Link to="/students">Students</Link></li><li>
                <Link to="/index">Home</Link></li>

              </ul>
        </div>

        <h1>Welcome!</h1>

        <br/>
        <br/>
        <p>
            Student progress tracker.<br/>
            All-in-one dashboard for tracking student engagement
        </p>

        {/* <button class="button buttong" onClick="window.location='import.html';">Import (Nor implemented)</button> */}
        <div>
        <Dragger {...uploadProps}>
        <p className="ant-upload-drag-icon">
          <InboxOutlined />
        </p>
        <p className="ant-upload-text">upload csv file</p>
      </Dragger>
      {nextStepVisible && (
        <Button type="primary" onClick={handleNextStep}>
          下一步
        </Button>
      )}
    </div>
  


        </div>

    )
}
export default Home;