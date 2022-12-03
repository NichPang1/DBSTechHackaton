import { GridComponent, ColumnsDirective, ColumnDirective, Page, Selection, Inject, Edit, Toolbar, Sort, Filter } from '@syncfusion/ej2-react-grids';

// import { customersData, customersGrid } from '../data/dummy';
import { scheduledTransactionsGrid } from '../data/dummyData';
import { Header } from '../components';
import { useEffect, useState } from "react";
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';


import axios from "axios";


const Customers = () => {
  const selectionsettings = { persistSelection: true };
  const toolbarOptions = ['Delete'];
  const editing = { allowDeleting: true, allowEditing: true };

  const baseURL = "http://127.0.0.1:5000/";
  const [transactions, setTransactions] = useState();


  useEffect(() => {
    axios.get(baseURL + "transactions").then((response) => {
      setTransactions(response.data);
    });
  });

  if (!transactions) return null;

  return (
<Box
      component="form"
      sx={{
        '& .MuiTextField-root': { m: 1, width: '25ch' },
      }}
      noValidate
      autoComplete="off"
    >
      <div>
        <TextField
          required
          id="outlined"
          label="Recipient Bank Account ID"
          defaultValue=""
        />
        <TextField
          required
          id="outlined"
          label="Transaction Amount"
          defaultValue=""
        />
      </div>
    </Box>
  );
};

export default Customers;
