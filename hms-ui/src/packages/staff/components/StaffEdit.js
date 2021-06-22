// Copyright (C) 2021 Ibrahem Mouhamad

import * as React from "react";
import { Edit, SimpleForm, TextInput, ReferenceInput, SelectInput, useTranslate } from 'react-admin';

const StaffEdit = props => {
    const tranlsate = useTranslate();
    return (
        <Edit {...props}>
            <SimpleForm>
                <SelectInput source="type" choices={[
                    { id: 'operation', name: tranlsate('resources.staff.type_option.operation') },
                    { id: 'administration', name: tranlsate('resources.staff.type_option.administration') },
                ]} />
                <TextInput source="name" />
                <TextInput source="speciality" />
                <ReferenceInput source="department" reference="department">
                    <SelectInput optionText="name" />
                </ReferenceInput>
            </SimpleForm>
        </Edit>
    );
};

export default StaffEdit;

