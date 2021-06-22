// Copyright (C) 2021 Ibrahem Mouhamad

import * as React from "react";
import { Create, SimpleForm, TextInput } from 'react-admin';

const HospitalCreate = props => (
    <Create {...props}>
        <SimpleForm>
            <TextInput source="name" />
            <TextInput source="address" />
            <TextInput source="phone_number" />
        </SimpleForm>
    </Create>
);

export default HospitalCreate;

