import React, { useState } from 'react';
import { Select } from 'antd';
import { Link } from "react-router-dom";
import { useSelector } from 'react-redux';
import { Table, Input, Button, Form } from 'antd';

const EditableCell = ({
  editing,
  dataIndex,
  title,
  inputType,
  record,
  index,
  children,
  ...restProps
}) => {
  return (
    <td {...restProps}>
      {editing ? (
        <Form.Item
          name={dataIndex}
          style={{ margin: 0 }}
          rules={[
            {
              required: true,
              message: `Please Input ${title}!`,
            },
          ]}
        >
          <Input />
        </Form.Item>
      ) : (
        children
      )}
    </td>
  );
};



const { Option } = Select;


const Students = () => {
  const [sortColumn, setSortColumn] = useState(null);
  const [sortOrder, setSortOrder] = useState('asc');
  const [filters, setFilters] = useState({});

  const importedData = useSelector((state) => state.importedData.scores);
  const [form] = Form.useForm();
  const assessments = useSelector((state) => state.importedData.assessments);

  // Generate a unique key for each column
  // const acolumns = assessments.map((assessment, index) => ({
  //   title: assessment,
  //   dataIndex: `assessment${index}`,
  //   key: `assessment${index}`,
  //   onCell: (record) => ({
  //     record,
  //     inputType: 'text',
  //     dataIndex: `assessment${index}`,
  //     title: assessment,
  //     editing: true, // We set it as true to have all text boxes editable
  //   }),
  // }));
  const acolumns = assessments.map((assessment, index) => ({
    title: assessment,
    dataIndex: assessment,
    key: assessment,
    onCell: (record) => ({
      record,
      inputType: 'text',
      dataIndex: assessment,
      title: assessment,
      editing: true, // We set it as true to have all text boxes editable
    }),
  }));

  // Mimic a single rowData with keys based on columns' dataIndex
  let initialRowData = {};
  acolumns.forEach(({ dataIndex }) => (initialRowData[dataIndex] = ''));
  const [data, setData] = React.useState([initialRowData]);

  const handleSave = () => {
    form.validateFields()
      .then((values) => {
        // TODO:
        // Here you would generally handle the submission of text box values (values)
        console.log(values);
      })
      .catch((info) => {
        console.log('Validate Failed:', info);
      });
  };


  const parsedData = importedData;

  const columns = parsedData.length > 0 ? Object.keys(parsedData[0]) : [];

  const getColorByInfo = (info) => {
    if (info.toLowerCase().includes("inconsistent")) return 'orange';
    if (info.toLowerCase().includes("failed")) return 'red';
    if (info.toLowerCase().includes("late")) return 'darkgreen';
    return 'black'; // Default color
  };

  const handleSort = (column, order) => {
    setSortColumn(column);
    setSortOrder(order);
  };

  const handleFilterChange = (column, values) => {
    setFilters((prevFilters) => ({
      ...prevFilters,
      [column]: values,
    }));
  };

  const filteredData = parsedData.filter((student) =>
  Object.entries(filters).every(
    ([column, filterValues]) =>
      filterValues.length === 0 || filterValues.includes('All') || filterValues.includes(student[column])
  )
);

  const sortedData = filteredData.sort((a, b) => {
    if (sortColumn) {
      const order = sortOrder === 'asc' ? 1 : -1;
      return (a[sortColumn] - b[sortColumn]) * order;
    }
    return b.Engagement - a.Engagement;
    
  });

  const exportToCSV = () => {
    const csvData = sortedData.map((student) =>
      columns.map((column) => student[column]).join(',')
    ).join('\n');

    const blob = new Blob([csvData], { type: 'text/csv;charset=utf-8' });
    const link = document.createElement('a');
    const fileName = 'table_data.csv';

    if (link.download !== undefined) {
      link.setAttribute('href', URL.createObjectURL(blob));
      link.setAttribute('download', fileName);
      link.style.visibility = 'hidden';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    } else {
      window.open(URL.createObjectURL(blob));
    }
  };


  const renderColumnHeader = (column) => {
    const filterValues = filters[column] || [];
    const options = Array.from(new Set(parsedData.map((student) => student[column]))).map(
      (value) => (
        <Option key={value} value={value}>
          {value}
        </Option>
      )
    );
  
    return (
      <th key={column}>
        {column}
        <Select
          mode="multiple"
          value={filterValues.includes('All') ? ['All'] : filterValues}
          onChange={(values) => handleFilterChange(column, values)}
          style={{ width: '200px' }}
          dropdownRender={(menu) => (
            <div>
              {menu}
              <div className="sort-buttons">
                <button onClick={() => handleSort(column, 'asc')}>Sort Ascending</button>
                <button onClick={() => handleSort(column, 'desc')}>Sort Descending</button>
              </div>
            </div>
          )}
        >
          <Option value="All">All</Option>
          {options}
        </Select>
      </th>
    );
  };
  return (
    <div className="App">
      <ul>{/* {channelList.map(item=> <li key={item.id}>{item.name}</li>)} */}</ul>
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
      <h1>Student</h1>

      <br></br>
      <div>
      <Form form={form} component={false}>
      <Table
        components={{
          body: {
            cell: EditableCell,
          },
        }}
        bordered
        dataSource={data}
        columns={acolumns}
        rowClassName="editable-row"
        pagination={false}
      />
      <Button onClick={handleSave} type="primary" style={{ marginTop: '20px' }}>
        Submit
      </Button>
    </Form>
      </div>


      <div className="table_background">
      <table id="main_table">
        <thead>
          <tr>{columns.map(renderColumnHeader)}</tr>
        </thead>
        <tbody>
      {sortedData.map((student, index) => (
        <tr key={index}>
          {columns.map((column, columnIndex) => {
            if (column === 'Info') {
              return (
                <td key={columnIndex}>
                  {student[column].map((info, infoIndex) => (
                    <div key={infoIndex} style={{ color: getColorByInfo(info[0]) }}>
                      {info[0]}: {info[1]}
                    </div>
                  ))}
                </td>
              );
            } else if (column === 'Failed Assessments') {
              return (
                <td key={columnIndex}>
                  {student[column].map((assi, assiIndex) => (
                    <div key={assiIndex}>
                      <span style={{ color: 'blue' }}>{assi[0]}</span>{' '}
                      <span style={{ color: 'red' }}>{assi[1]}</span>
                    </div>
                  ))}
                </td>
              );
            } else if (column === 'Late Submissions') {
              return (
                <td key={columnIndex}>
                  {student[column].map((assi, assiIndex) => (
                    <div key={assiIndex}>
                      <span style={{ color: 'blue' }}>{assi[0]}</span>{' '}
                      <span style={{ color: 'red' }}>{assi[1]}</span>
                    </div>
                  ))}
                </td>
              );
            } else {
              return <td key={columnIndex}>{student[column]}</td>;
            }
          })}
        </tr>
      ))}
    </tbody>
      </table>
    </div>


    
    <br />
    <button className="button buttong" onClick={exportToCSV}>
        Export (currently filtered table)
      </button>
      
    </div>
  );
};

export default Students;