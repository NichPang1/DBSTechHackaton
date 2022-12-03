import { AiOutlineCalendar, AiOutlineShoppingCart, AiOutlineAreaChart, AiOutlineBarChart, AiOutlineStock } from 'react-icons/ai';
import { FiShoppingBag, FiEdit, FiPieChart, FiBarChart, FiCreditCard, FiStar, FiShoppingCart } from 'react-icons/fi';
import { BsKanban, BsBarChart, BsBoxSeam, BsCurrencyDollar, BsShield, BsChatLeft } from 'react-icons/bs';
import { IoMdContacts } from 'react-icons/io';
import { RiContactsLine, RiStockLine } from 'react-icons/ri';


export const scheduledTransactionsGrid = [
    { field: 'AccountID',
      headerText: 'Account ID',
      width: '150',
      textAlign: 'Center' },
    { field: 'ReceivingAccountID',
      headerText: 'Receiving Account ID',
      width: '150',
      textAlign: 'Center' },
    { field: 'Date',
      headerText: 'Date',
      width: '150',
      textAlign: 'Center' },
    { field: 'TransactionAmount',
      headerText: 'Transaction Amount',
      width: '150',
      textAlign: 'Center' },
    { field: 'Comment',
      headerText: 'Comment',
      width: '150',
      textAlign: 'Center' }
  ]

export const links = [
    {
      title: 'Pages',
      links: [
        {
          name: 'transactions',
          icon: <AiOutlineShoppingCart />,
        },
        {
          name: 'employees',
          icon: <IoMdContacts />,
        },
        {
          name: 'customers',
          icon: <RiContactsLine />,
        },
      ],
    }
  ];
