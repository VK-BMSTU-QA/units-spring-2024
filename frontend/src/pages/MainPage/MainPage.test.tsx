import React from 'react';
import { MainPage } from "./MainPage";
import { render, fireEvent } from '@testing-library/react';
import { useCurrentTime, useProducts } from '../../hooks';
import {  Category, Product } from '../../types';
import { applyCategories, updateCategories } from '../../utils';

const testProducts = [
    {
    id:1,
    name:'Product',
    description:'description',
    price:1000,
    category:'Одежда' as Category,
    } as Product
];

jest.mock('../../hooks/useCurrentTime', () => ({
    useCurrentTime: jest.fn(() => "18:00:00"),
}));

jest.mock('../../hooks/useProducts', () => ({
    useProducts: jest.fn(() => { return testProducts}),
}));

jest.mock('../../utils/updateCategories', () => ({
    updateCategories: jest.fn(() => ['Одежда'as Category] ),
}));

jest.mock('../../utils/applyCategories', () => ({
    applyCategories: jest.fn(() => { return testProducts}),
}));

afterEach(jest.clearAllMocks);

describe('Categories test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call useProducts, useCurrentTime, applyCategories', () => {
        const rendered = render(<MainPage />);

        expect(useProducts).toBeCalledTimes(1);
        expect(useCurrentTime).toBeCalledTimes(1);
        expect(applyCategories).toBeCalledTimes(1);
    });

    it('should call updateCategories onClick', () => {
        const rendered = render(<MainPage />);
  
        const allCategories = rendered.getAllByText(testProducts[0].category)

        for (const target of allCategories) {
            if (target.classList.contains('categories__badge'))  {
                fireEvent.click(target);
                break;
            }
        }

        expect(updateCategories).toBeCalledTimes(1);
    });
});
