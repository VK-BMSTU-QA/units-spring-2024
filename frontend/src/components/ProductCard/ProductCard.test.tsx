import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types';
import { getPrice } from '../../utils';

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
    __esModule: true,
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