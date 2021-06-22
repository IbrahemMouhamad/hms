// Copyright (C) 2021 Ibrahem Mouhamad

import * as React from "react";
import { Create, SimpleForm, TextInput, ReferenceInput, SelectInput } from 'react-admin';

const DepartmentCreate = props => (
    <Create {...props}>
        <SimpleForm>
        <TextInput source="name" />
            <ReferenceInput source="hospital" reference="hospital">
                <SelectInput optionText="name" />
            </ReferenceInput>
        </SimpleForm>
    </Create>
);

export default DepartmentCreate;

