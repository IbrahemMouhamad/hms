// Copyright (C) 2021 Ibrahem Mouhamad

import englishMessages from 'ra-language-english';

const hmsEnglishMessages = {
    ...englishMessages,
    resources: {
        hospital: {
            name: 'Hospital  |||| Hospitals',
            fields: {
                name: "Name",
                address: "Address",
                phone_number: "Phone Number",
            }
        },
        department: {
            name: 'Department  |||| Departments',
            fields: {
                name: "Name",
                hospital: "Hospital",
            }
        },
        staff: {
            name: 'Staff  |||| Staffs',
            fields: {
                type: 'Type',
                name: "Name",
                speciality: "Speciality",
                department: "Department",
            },
            type_option: {
                operation: "Operational",
                administration: "Administrative",
            }
        },
    },
    action: {
        local_switcher: {
            label: 'Language',
            en_label: 'English',
            ru_label: 'Russian',
        },
    },
}

export default hmsEnglishMessages