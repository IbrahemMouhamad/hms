// Copyright (C) 2021 Ibrahem Mouhamad

import * as React from 'react';
import { Layout } from 'react-admin';
import CustomAppBar from './AppBar';

const CustomLayout = (props) => <Layout {...props} appBar={CustomAppBar} />;

export default CustomLayout;