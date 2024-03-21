import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types';
import { getPrice } from '../../utils';

afterEach(jest.clearAllMocks);

jest.mock('../../utils', () => ({
    applyCategories: jest.fn((products, categories) => products),
    updateCategories: jest.fn((selectedCategories, clickedCategory) => [
        ...selectedCategories,
        clickedCategory,
    ]),
    getPrice: jest.fn((price, priceSymbol) => `${price} ${priceSymbol}`),
}));

const products: Product[] = [
    {
        id: 1,
        name: 'Название',
        description: 'Описание',
        price: 128,
        priceSymbol: '$',
        imgUrl: 'url',
        category: 'Одежда',
    },
    {
        id: 1,
        name: 'Название',
        description: 'Описание',
        price: 128,
        priceSymbol: '$',
        imgUrl: '',
        category: 'Одежда',
    },
];

describe('Product card test', () => {
    it('should render correctly', () => {
        expect(getPrice).toHaveBeenCalledTimes(0);

        const rendered = render(<ProductCard {...products[0]} />);

        expect(getPrice).toHaveBeenCalledTimes(1);
        expect(rendered.asFragment()).toMatchSnapshot();
        expect(rendered.container.querySelector('img')).toBeInTheDocument();
    });

    test('does not render image if imgUrl is not provided', () => {
        const rendered = render(<ProductCard {...products[1]} />);

        expect(rendered.asFragment()).toMatchSnapshot();
        expect(rendered.container.querySelector('img')).not.toBeInTheDocument();
    });
});
