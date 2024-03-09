import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types/Product';
import { getPrice } from '../../utils';

afterEach(jest.clearAllMocks);
describe('Product card test', () => {
    it('should render correctly', () => {
      let prod: Product = {
          id: 1,
          name: 'IPhone 14 Pro',
          description: 'Latest iphone, buy it now',
          price: 999,
          priceSymbol: '$',
          category: 'Электроника',
          imgUrl: '/iphone.png',
      }
      const rendered = render(
        <ProductCard 
          id = {prod.id}
          name = {prod.name}
          description = {prod.description}
          price = {prod.price}
          priceSymbol = {prod.priceSymbol}
          category = {prod.category}
          imgUrl= {prod.imgUrl}
        />
      );
      expect(rendered.container.querySelector('.product-card__name')).toHaveTextContent(prod.name)
      expect(rendered.container.querySelector('.product-card__description')).toHaveTextContent(prod.description)
      expect(rendered.container.querySelector('.product-card__price')).toHaveTextContent(getPrice(prod.price, prod.priceSymbol))
      expect(rendered.container.querySelector('.product-card__category')).toHaveTextContent(prod.category)
      expect(rendered.container.querySelector('.product-card__image')).toHaveAttribute('src', prod.imgUrl)
      expect(rendered.container.querySelector('.product-card__image')).toHaveAttribute('alt', prod.name)
    });
});
