import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { getPrice } from '../../utils';
import { Product } from '../../types';
import { ProductCard } from './ProductCard';

const testProduct: Product = {
    id: 1,
    name: 'IPhone 14 Pro',
    description: 'Latest iphone, buy it now',
    price: 999,
    priceSymbol: '$',
    category: 'Электроника',
    imgUrl: '/iphone.png',
};

jest.mock('../../utils/getPrice', () => ({
    getPrice: jest.fn(() => '999 $'),
}));

afterEach(jest.clearAllMocks);
describe('ProductСard test', () => {
    it('should render correctly', () => {
        const rendered= render(
            <ProductCard
                key={testProduct.id}
                {...testProduct}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call get price', () => {
        render(
            <ProductCard
                key={testProduct.id}
                {...testProduct}
            />
        );

        expect(getPrice).toHaveBeenCalledTimes(1);
    });
});