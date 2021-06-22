// Copyright (C) 2021 Ibrahem Mouhamad

import * as React from "react";
import { Edit, SimpleForm, TextInput } from 'react-admin';

const HospitalEdit = props => (
    <Edit {...props}>
        <SimpleForm>
            <TextInput source="name" />
            <TextInput source="address" />
            <TextInput source="phone_number" />
        </SimpleForm>
    </Edit>
);

export default HospitalEdit;

