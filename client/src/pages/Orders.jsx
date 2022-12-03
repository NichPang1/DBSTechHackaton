// SCHEDULED TRANSACTIONS

import { GridComponent, ColumnsDirective, ColumnDirective, Page, Selection, Inject, Edit, Toolbar, Sort, Filter } from '@syncfusion/ej2-react-grids';
import { AiOutlineCalendar, AiOutlineShoppingCart, AiOutlineAreaChart, AiOutlineBarChart, AiOutlineStock } from 'react-icons/ai';

// import { customersData, customersGrid } from '../data/dummy';
import { BrowserRouter, Routes, Route, useNavigate } from 'react-router-dom';
import { scheduledTransactionsGrid } from '../data/dummyData';
import { Header } from '../components';
import { useEffect, useState } from "react";
import Button from '@mui/material/Button';
import Box from '@mui/material/Box';
import { DataGrid, GridColDef, GridValueGetterParams } from '@mui/x-data-grid';
import axios from "axios";


const Orders = () => {
  const selectionsettings = { persistSelection: true };
  const toolbarOptions = ['Delete'];
  const editing = { allowDeleting: true, allowEditing: true };
  

  const baseURL = "http://127.0.0.1:5000/";
  const [transactions, setTransactions] = useState();

  const navigate = useNavigate();

  useEffect(() => {
    axios.get(baseURL + "transactions").then((response) => {
      setTransactions(response.data);
    });
  });

  if (!transactions) return null;

  return (
    <Box sx={{ height: 400, width: '100%' }}>
      <Button variant="contained"
        onClick={() => {
          navigate("/addNewTransaction");
        }}>Add</Button>
      <DataGrid
        rows={transactions}
        columns={scheduledTransactionsGrid}
        getRowId={(row) => row.TransactionID}
        pageSize={5}
        rowsPerPageOptions={[5]}
        checkboxSelection
      />
    </Box>
  );
};

export default Orders;
