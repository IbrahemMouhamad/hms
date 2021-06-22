// Copyright (C) 2021 Ibrahem Mouhamad

import * as React from "react";
import { List, Datagrid, TextField, ReferenceField } from 'react-admin';

const DepartmentList = props => (
    <List {...props}>
        <Datagrid rowClick="edit">
            <TextField source="name" />
            <ReferenceField source="hospital" reference="hospital">
                <TextField source="name" />
            </ReferenceField>
        </Datagrid>
    </List>
);

export default DepartmentList;