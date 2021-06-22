// Copyright (C) 2021 Ibrahem Mouhamad

import russianMessages from 'ra-language-russian';

const hmsRussianMessages = {
    ...russianMessages,
    resources: {
        hospital: {
            name: 'Больница  |||| Больницы',
            fields: {
                name: "Имя",
                address: "Адрес",
                phone_number: "Номер Телефона",
            },
        },
        department: {
            name: 'Отдел  |||| Отделы',
            fields: {
                name: "Имя",
                hospital: "Больница",
            }
        },
        staff: {
            name: 'Персонал  |||| Персонал',
            fields: {
                type: 'Тип',
                name: "Имя",
                speciality: "Специальность",
                department: "Отдел",
            },
            type_option: {
                operation: "Оперативный",
                administration: "административный",
            }
        },
    },
    action: {
        local_switcher: {
            label: 'Язык',
            en_label: 'Английский',
            ru_label: 'Русский',
        },
    },
}

export default hmsRussianMessages