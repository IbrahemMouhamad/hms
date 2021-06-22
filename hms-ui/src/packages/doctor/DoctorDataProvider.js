// Copyright (C) 2021 Ibrahem Mouhamad
import { stringify } from 'query-string';

import { fetchJsonWithAuthToken, getOneJson, getPaginationQuery, getFilterQuery, getOrderingQuery } from "../common";

const apiUrl = process.env.REACT_APP_API_URL + process.env.REACT_APP_DOCTOR_PATH;

const dataProvider = {
    getList: async (resource, params) => {
        const query = {
            ...getFilterQuery(params.filter),
            ...getPaginationQuery(params.pagination),
            ...getOrderingQuery(params.sort),
        };
        const url = `${apiUrl}?${stringify(query)}`;

        const { json } = await fetchJsonWithAuthToken(url);

        return {
            data: json.results,
            total: json.count,
        };
    },

    getOne: async (resource, params) => {
        const data = await getOneJson(apiUrl, params.id);
        return {
            data,
        };
    },

    getMany: (resource, params) => {
        return Promise.all(
            params.ids.map(id => getOneJson(apiUrl, id))
        ).then(data => ({ data }));
    },

    getManyReference: async (resource, params) => {
        const query = {
            ...getFilterQuery(params.filter),
            ...getPaginationQuery(params.pagination),
            ...getOrderingQuery(params.sort),
            [params.target]: params.id,
        };
        const url = `${apiUrl}?${stringify(query)}`;

        const { json } = await fetchJsonWithAuthToken(url);
        return {
            data: json.results,
            total: json.count,
        };
    },

    update: async (resource, params) => {
        const { json } = await fetchJsonWithAuthToken(`${apiUrl}/${params.id}`, {
            method: 'PATCH',
            body: JSON.stringify(params.data),
        });
        return { data: json };
    },

    updateMany: (resource, params) =>
        Promise.all(
            params.ids.map(id =>
                fetchJsonWithAuthToken(`${apiUrl}/${id}/`, {
                method: 'PATCH',
                body: JSON.stringify(params.data),
            })
            )
        ).then(responses => ({ data: responses.map(({ json }) => json.id) })),

    create: async (resource, params) => {
        const { json } = await fetchJsonWithAuthToken(`${apiUrl}`, {
            method: 'POST',
            body: JSON.stringify(params.data),
        });
        return {
            data: { ...json },
        };
    },

    delete: (resource, params) =>
        fetchJsonWithAuthToken(`${apiUrl}/${params.id}`, {
            method: 'DELETE',
        }).then(() => ({ data: [] })),

    deleteMany: (resource, params) =>
        Promise.all(
            params.ids.map(id =>
                fetchJsonWithAuthToken(`${apiUrl}/${id}`, {
                method: 'DELETE',
            })
            )
        ).then(responses => ({ data: [] })),
};

export default dataProvider