import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';
import { Product } from '../../types/Product';
import { getPrice } from '../../utils';

jest.mock('../../utils/getPrice', () => ({
  getPrice: jest.fn(() => '999 $')
}));


const prod: Product = {
  id: 1,
  name: 'IPhone 14 Pro',
  description: 'Latest iphone, buy it now',
  price: 999,
  priceSymbol: '$',
  category: 'Электроника',
  imgUrl: '/iphone.png',
}

afterEach(jest.clearAllMocks);
describe('Product card test', () => {
    it('should render correctly with image', () => {
      const rendered = render(
        <ProductCard 
          {...prod}
        />
      );
      expect(rendered.container.querySelector('.product-card__name')).toHaveTextContent(prod.name)
      expect(rendered.container.querySelector('.product-card__description')).toHaveTextContent(prod.description)
      expect(rendered.container.querySelector('.product-card__price')).toHaveTextContent(getPrice(prod.price, prod.priceSymbol))
      expect(rendered.container.querySelector('.product-card__category')).toHaveTextContent(prod.category)
      expect(rendered.container.querySelector('.product-card__image')).toHaveAttribute('src', prod.imgUrl)
      expect(rendered.container.querySelector('.product-card__image')).toHaveAttribute('alt', prod.name)

      expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should render correctly without image', () => {
      const rendered = render(
        <ProductCard 
          {...prod}
          imgUrl= {undefined}
        />
      );
      expect(rendered.container.querySelector('.product-card__name')).toHaveTextContent(prod.name)
      expect(rendered.container.querySelector('.product-card__description')).toHaveTextContent(prod.description)
      expect(rendered.container.querySelector('.product-card__price')).toHaveTextContent(getPrice(prod.price, prod.priceSymbol))
      expect(rendered.container.querySelector('.product-card__category')).toHaveTextContent(prod.category)

      expect(rendered.asFragment()).toMatchSnapshot();
    });


    it('should call getPrice', () => {
      render(<ProductCard 
          {...prod} 
           />)

      expect(getPrice).toBeCalledWith(prod.price, prod.priceSymbol)
      expect(getPrice).toHaveBeenCalledTimes(1)
  });
});
