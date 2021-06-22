// Copyright (C) 2021 Ibrahem Mouhamad

import React, {useState} from 'react';
import { useLocale, useSetLocale, useTranslate, Button } from 'react-admin';
import Tooltip from '@material-ui/core/Tooltip';
import Menu from '@material-ui/core/Menu';
import Translate from '@material-ui/icons/Translate';
import { MenuItemLink } from 'react-admin';

const LocaleSwitcher = ({className, ...props}) => {
    const [anchorEl, setAnchorEl] = useState(null);
    const open = Boolean(anchorEl);
    const locale = useLocale();
    const setLocale = useSetLocale();
    const translate = useTranslate();
    return (
        <div className={className}>
            <Tooltip title={translate('action.local_switcher.label')}>
                <Button
                    aria-label={translate('action.local_switcher.label')}
                    aria-owns={open ? 'menu-appbar' : null}
                    aria-haspopup={true}
                    color="inherit"
                    onClick={ event => { setAnchorEl(event.currentTarget); } }
                    label={translate('action.local_switcher.label')}
                >
                    <Translate />
                </Button>
            </Tooltip>
            <Menu
                id="menu-appbar"
                anchorEl={anchorEl}
                anchorOrigin={{
                    vertical: 'top',
                    horizontal: 'right',
                }}
                transformOrigin={{
                    vertical: 'top',
                    horizontal: 'right',
                }}
                open={open}
                onClose={ () => { setAnchorEl( null ); } }
            >
                <MenuItemLink
                    to="#"
                    disabled={locale === 'en'}
                    onClick={() => {
                            setLocale('en');
                            localStorage.setItem('locale','en');
                            setAnchorEl( null );
                        }
                    }
                    primaryText={translate('action.local_switcher.en_label')}
                />
                <MenuItemLink
                    to="#"
                    disabled={locale === 'ru'}
                    onClick={() => {
                            setLocale('ru');
                            localStorage.setItem('locale','de');
                            setAnchorEl( null );
                        }
                    }
                    primaryText={translate('action.local_switcher.ru_label')}
                />
            </Menu>
        </div>
    );
};

export default LocaleSwitcher;