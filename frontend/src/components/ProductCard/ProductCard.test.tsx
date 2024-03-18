import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { getPrice } from '../../utils';
import { Product } from '../../types';
import { ProductCard } from './ProductCard';

const testProduct: Product = {
    id: 1,
    name: 'my product',
    description: 'description of product',
    price: 1000,
    priceSymbol: "₽",
    category: 'Одежда',
    imgUrl: 'imgurl.png'
};

afterEach(jest.clearAllMocks);

jest.mock('../../utils/getPrice', () => ({
    getPrice: jest.fn(() => "1\xa0000 ₽"),
}));

describe('ProductCard test', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard 
            {...testProduct} 
             />);

        expect(rendered.asFragment()).toMatchSnapshot();

        expect(rendered.queryByRole('img')).toBeTruthy();
    });

    it('should render correctly without imgUrl', () => {
        const rendered = render(<ProductCard 
            {...testProduct} 
            imgUrl={undefined}
             />);

        expect(rendered.asFragment()).toMatchSnapshot();

        expect(rendered.queryByRole('img')).toBeNull();
    });

    it('should getPrice called', () => {
        render(<ProductCard 
            {...testProduct} 
             />)

        expect(getPrice).toHaveBeenCalledTimes(1)
    });
});
