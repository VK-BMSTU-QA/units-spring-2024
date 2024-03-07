import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import type { Product } from '../../types';

afterEach(jest.clearAllMocks);
describe('ProductCard test', () => {
    const product: Product = {
        id: 1,
        name: 'Телефон',
        description: 'Описание продукта 1',
        price: 100,
        category: 'Электроника',
      };

    it('should render product information correctly', () => {
        const rendered = render(<ProductCard {...product} />);
        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('renders product name', () => {
        const { getByText } = render(<ProductCard {...product} />);
        expect(getByText('Телефон')).toBeInTheDocument();
      });
      
      it('displays product description', () => {
        const { getByText } = render(<ProductCard {...product} />);
        expect(getByText('Описание продукта 1')).toBeInTheDocument();
      });
      
      it('displays product category', () => {
        const { getByText } = render(<ProductCard {...product} />);
        expect(getByText('Электроника')).toBeInTheDocument();
      });
      
      it('displays product image when imgUrl is provided', () => {
        const productWithImage = { ...product, imgUrl: 'test-image.jpg' };
        const { getByAltText } = render(<ProductCard {...productWithImage} />);
        expect(getByAltText('Телефон')).toBeInTheDocument();
      });
      
      it('does not display product image when imgUrl is not provided', () => {
        const { queryByAltText } = render(<ProductCard {...product} />);
        expect(queryByAltText('Телефон')).not.toBeInTheDocument();
      });
});