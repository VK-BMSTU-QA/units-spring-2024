import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
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

describe('Product card test', () => {
    it('should render correctly', () => {

        expect(getPrice).toHaveBeenCalledTimes(0);

        const rendered = render(
            <ProductCard
                name={'name'}
                description={'desc'}
                category={'Одежда'}
                price={123}
                id={1}
                imgUrl={'qwwe'}
            />
        );

        expect(getPrice).toHaveBeenCalledTimes(1);
        
        expect(rendered.asFragment()).toMatchSnapshot();

        expect(rendered.container.querySelector('img')).toBeInTheDocument();
    });

    test('does not render image if imgUrl is not provided', () => {
        const rendered = render(
            <ProductCard
                name={'name'}
                description={'desc'}
                category={'Одежда'}
                price={123}
                id={1}
                imgUrl={''}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();

        expect(rendered.container.querySelector('img')).not.toBeInTheDocument();
    });
});