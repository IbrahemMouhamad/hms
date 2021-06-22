// Copyright (C) 2021 Ibrahem Mouhamad

import * as React from 'react';
import { AppBar } from 'react-admin';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';
import LocaleSwitcher from '../button/LocaleSwitcher';

const useStyles = makeStyles({
    spacer: {
        flex: 1,
    },
});

const CustomAppBar = props => {
    const classes = useStyles();
    return (
        <AppBar {...props}>
            <Typography
                variant="h6"
                color="inherit"
                id="react-admin-title"
            />
            <span className={classes.spacer} />
            <LocaleSwitcher />
        </AppBar>
    );
};

export default CustomAppBar;