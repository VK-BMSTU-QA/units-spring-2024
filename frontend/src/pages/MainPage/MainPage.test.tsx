import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import { useCurrentTime, useProducts } from '../../hooks';
import { applyCategories, updateCategories } from '../../utils';

jest.mock('../../hooks/useCurrentTime', () => ({
  useCurrentTime: jest.fn(() => '00:00:00'),
}));
jest.mock('../../hooks/useProducts', () => ({
  useProducts: jest.fn(() => [{
    id: 1,
    name: 'IPhone 14 Pro',
    description: 'Latest iphone, buy it now',
    price: 999,
    priceSymbol: '$',
    category: 'Электроника',
    imgUrl: '/iphone.png',
  }]),
}));
jest.mock('../../utils/applyCategories', () => ({
  applyCategories: jest.fn(() => [{
    id: 1,
    name: 'IPhone 14 Pro',
    description: 'Latest iphone, buy it now',
    price: 999,
    priceSymbol: '$',
    category: 'Электроника',
    imgUrl: '/iphone.png',
  }])
}));
jest.mock('../../utils/updateCategories', () => ({
  updateCategories: jest.fn(() => [{
    id: 1,
    name: 'IPhone 14 Pro',
    description: 'Latest iphone, buy it now',
    price: 999,
    priceSymbol: '$',
    category: 'Электроника',
    imgUrl: '/iphone.png',
  }])
}));

afterEach(() => { 
  jest.clearAllMocks();
});
describe('Main page test', () => {
    it('should render correclty', () => {
      const rendered = render(<MainPage />);

      expect(rendered.getByText('VK Маркет')).toHaveClass('main-page__title');
      expect(rendered.getByText('00:00:00')).toContainHTML('<h3>00:00:00</h3>');
      expect(rendered.asFragment()).toMatchSnapshot();
    });
    it('should call Hooks', () => {
      const rendered = render(<MainPage />);
      expect(useCurrentTime).toHaveBeenCalledTimes(1);
      expect(useProducts).toHaveBeenCalledTimes(1);
    });
    it('should call applyCategories', () => {
      const rendered = render(<MainPage />);
      expect(applyCategories).toHaveBeenCalledTimes(1);
    });
    it('should call updateCategories', () => {
      const rendered = render(<MainPage />);
      fireEvent.click(rendered.getByText('Одежда'));
      expect(updateCategories).toHaveBeenCalledTimes(1);
    });
});
