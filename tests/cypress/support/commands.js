// Copyright (C) 2021 Ibrahem Mouhamad

Cypress.Commands.add('login', (username = Cypress.env('user'), password = Cypress.env('password')) => {
    cy.get('[type="text"]').clear().type(username);
    cy.get('[type="password"]').clear().type(password);
    cy.get('[type="submit"]').click();
    cy.url().should('match', /\/hospital$/);
});

Cypress.Commands.add('logout', (username = Cypress.env('user')) => {
    cy.get('button[aria-label="Profile"]').click();
    cy.get('.logout').click();
    cy.url().should('include', '/login');
    cy.visit('/login'); // clear query parameter "next"
});