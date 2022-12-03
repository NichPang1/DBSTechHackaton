import { GridComponent, ColumnsDirective, ColumnDirective, Page, Selection, Inject, Edit, Toolbar, Sort, Filter } from '@syncfusion/ej2-react-grids';

// import { customersData, customersGrid } from '../data/dummy';
import { scheduledTransactionsGrid } from '../data/dummyData';
import { Header } from '../components';
import { useEffect, useState } from "react";
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';



import axios from "axios";


const Customers = () => {
  const selectionsettings = { persistSelection: true };
  const toolbarOptions = ['Delete'];
  const editing = { allowDeleting: true, allowEditing: true };

  const baseURL = "http://127.0.0.1:5000/";
  const [transactions, setTransactions] = useState();
  const [ID, setID] = useState();
  const [transactionAmount, setTransactionAmount] = useState();
  const [comment, setComment] = useState();



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
          onChange={e => setID(e.target.value)}
        />
        <TextField
          required
          id="outlined"
          label="Transaction Amount"
          defaultValue=""
          onChange={e => setTransactionAmount(e.target.value)}
        />
        <TextField
          id="outlined"
          label="Comments"
          defaultValue=""
          onChange={e => setComment(e.target.value)}
        />
        {/* <Button
        onClick={() => {
          alert('clicked');
        }}
      ></Button> */}
      </div>

    </Box>
  );
};

export default Customers;
