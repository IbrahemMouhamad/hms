// Copyright (C) 2021 Ibrahem Mouhamad
import { fetchJsonWithAuthToken } from './tokenAuthProvider';
import { HospitalDataProvider } from "../hospital";
import { DepartmentDataProvider } from "../department";
import { StaffDataProvider } from "../staff";
import { DoctorDataProvider } from "../doctor";


const dataProvider = {
    getList:    (resource, params) => providers[resource].getList(resource, params),
    getOne:     (resource, params) => providers[resource].getOne(resource, params),
    getMany:    (resource, params) => providers[resource].getMany(resource, params),
    getManyReference: (resource, params) => providers[resource].getManyReference(resource, params),
    create:     (resource, params) => providers[resource].create(resource, params),
    update:     (resource, params) => providers[resource].update(resource, params),
    updateMany:     (resource, params) => providers[resource].updateMany(resource, params),
    delete:     (resource, params) => providers[resource].delete(resource, params),
    deleteMany:     (resource, params) => providers[resource].deleteMany(resource, params),
};

const providers = {
    hospital: HospitalDataProvider,
    department: DepartmentDataProvider,
    staff: StaffDataProvider,
    doctor: DoctorDataProvider,
};
export default dataProvider;

export const getOneJson = (apiUrl, id) =>
  fetchJsonWithAuthToken(`${apiUrl}/${id}`).then(
    (response) => response.json
  );

export const getPaginationQuery = (pagination) => {
    return {
      page: pagination.page,
      page_size: pagination.perPage,
    };
};

export const getFilterQuery = (filter) => {
    const { q: search, ...otherSearchParams } = filter;
    return {
      ...otherSearchParams,
      search,
    };
};

export const getOrderingQuery = (sort) => {
    const { field, order } = sort;
    return {
      ordering: `${order === 'ASC' ? '' : '-'}${field}`,
    };
};