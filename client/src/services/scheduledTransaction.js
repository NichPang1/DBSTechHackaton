import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react';

const baseUrl = 'http://127.0.0.1:5000/';

const createRequest = (url) => ({url})

export const userDetailsApi = createApi({
    reducerPath: 'userDetails',
    baseQuery: fetchBaseQuery({ baseUrl }),
    endpoints: (builder) => ({
        getCrypto: builder.query({
            query: ({ email, address, userId }) => createRequest(`userDetails?email=${email}&address=${address}&userId=${userId}`)
        }),
        
    })
});

export const {
    useGetUserDetailsQuery
} = userDetailsApi