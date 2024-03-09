import React from 'react';
import { Product } from '../../types';
import { ProductCard } from './ProductCard';
import { render } from '@testing-library/react';
import * as getPriceUtil from '../../utils/getPrice';

describe('ProductCard test', () => {
    const productProps: Product = {
        id: 0,
        name: 'Product name',
        description: 'This product is unbelievable',
        price: 999,
        priceSymbol: '$',
        category: 'Электроника',
        imgUrl: '/kitty.png',
    };

    it('should render correctly', () => {
        const rendered = render(<ProductCard {...productProps} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should call once getPrice util', () => {
        const mockGetPrice = jest.spyOn(getPriceUtil, 'getPrice');
        expect(mockGetPrice).not.toBeCalled();
        render(<ProductCard {...productProps} />);
        expect(mockGetPrice).toBeCalledTimes(1);
    });
});
