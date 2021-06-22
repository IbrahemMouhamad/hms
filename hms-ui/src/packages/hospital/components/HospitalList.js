// Copyright (C) 2021 Ibrahem Mouhamad

import * as React from "react";
import { List, Datagrid, TextField } from 'react-admin';

const HospitalList = props => (
    <List {...props}>
        <Datagrid rowClick="edit">
            <TextField source="name" />
            <TextField source="address" />
            <TextField source="phone_number" />
        </Datagrid>
    </List>
);

export default HospitalList;