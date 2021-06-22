// Copyright (C) 2021 Ibrahem Mouhamad

/// <reference types="cypress" />


context('When clicking on the Logout button, get the user session closed.', () => {

    function login(userName, password) {
        cy.get('[type="text"]').clear().type(userName);
        cy.get('[type="password"]').clear().type(password);
        cy.get('[type="submit"]').click();
    }

    before(() => {
        cy.visit('login');
    });

    describe("Testing Login", () => {
        it('Login', () => {
            cy.login();
        });

        it('Logout', () => {
            cy.logout();
        });

        it('Logout and login via GUI', () => {
            cy.login();
            // logout
            cy.get('button[aria-label="Profile"]').click();
            cy.get('.logout').click();
            cy.url().should('include', "/login");
            // login
            login(Cypress.env('user'), Cypress.env('password'));
            cy.url().should('include', "/hospital");
        });

        it('Incorrect user and correct password', () => {
            cy.logout();
            login('randomUser123', Cypress.env('password'));
            cy.url().should('include', '/login');
        });

        it('Correct user and incorrect password', () => {
            login(Cypress.env('user'), 'randomPassword123');
            cy.url().should('include', '/login');
        });

        it('Incorrect user and incorrect password', () => {
            login('randomUser123', 'randomPassword123');
            cy.url().should('include', '/login');
        });
    });
});