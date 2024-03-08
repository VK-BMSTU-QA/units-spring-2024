import React from 'react';
import { render } from '@testing-library/react';
import { ProductCard } from './ProductCard';
import '@testing-library/jest-dom';
import { PriceSymbol } from '../../types/Symbol';
import { Product } from '../../types/Product';

describe('ProductCard', () => {
  it('renders correctly', () => {
    const product: Product = {
        id: 1,
        name: 'Test Product',
        description: 'Test Description',
        price: 100,
        priceSymbol: '$',
        category: 'Электроника',
        imgUrl: 'https://example.com/test-image.jpg',
    };

    const { asFragment } = render(<ProductCard {...product} />);
    expect(asFragment()).toMatchSnapshot();
  });

  it('renders correctly without an image', () => {
    const productWithoutImage: Product = {
        id: 2,
        name: 'Test Product',
        description: 'Test Description',
        price: 100,
        priceSymbol: '$',
        category: 'Электроника',
      // imgUrl is intentionally left out
    };

    const { asFragment } = render(<ProductCard {...productWithoutImage} />);
    expect(asFragment()).toMatchSnapshot();
  });
});