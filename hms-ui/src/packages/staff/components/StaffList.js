// Copyright (C) 2021 Ibrahem Mouhamad

import * as React from "react";
import { List, Datagrid, TextField, ReferenceField } from 'react-admin';

const StaffList = props => (
    <List {...props}>
        <Datagrid rowClick="edit">
            <TextField source="type" />
            <TextField source="name" />
            <TextField source="speciality" />
            <ReferenceField source="department" reference="department">
                <TextField source="name" />
            </ReferenceField>
        </Datagrid>
    </List>
);

export default StaffList;