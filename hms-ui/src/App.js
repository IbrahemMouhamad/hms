import * as React from "react";
import { Admin, Resource, ListGuesser, EditGuesser  } from 'react-admin';
import polyglotI18nProvider from 'ra-i18n-polyglot';

import { DataProvider, tokenAuthProvider, Layout } from './packages/common';
import { HospitalList, HospitalEdit, HospitalCreate } from './packages/hospital';
import { DepartmentList, DepartmentEdit, DepartmentCreate } from './packages/department';
import { StaffList, StaffEdit, StaffCreate } from './packages/staff';
import hmsRussianMessages from './packages/i18n/ru';
import hmsEnglishMessages from './packages/i18n/en';

const messages = {
    ru: hmsRussianMessages,
    en: hmsEnglishMessages,
};
const locale = localStorage.getItem('locale');
const i18nProvider = polyglotI18nProvider(locale => messages[locale]);

const authProvider = tokenAuthProvider(
    process.env.REACT_APP_API_URL + process.env.REACT_APP_LOGIN_PATH
);

const App = () => (
    <Admin
        locale={locale}
        authProvider={authProvider}
        dataProvider={DataProvider}
        i18nProvider={i18nProvider}
        layout={Layout}
    >
        <Resource name="hospital" list={HospitalList} edit={HospitalEdit} create={HospitalCreate} />
        <Resource name="department" list={DepartmentList} edit={DepartmentEdit} create={DepartmentCreate} />
        <Resource name="staff" list={StaffList} edit={StaffEdit} create={StaffCreate} />
    </Admin>
);

export default App;
