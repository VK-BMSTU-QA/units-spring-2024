import React from 'react';
import { render, fireEvent } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';

jest.mock('../../hooks');
jest.mock('../../utils');
import * as hooks from '../../hooks';
import * as utils from '../../utils';

afterEach(() => { 
  jest.restoreAllMocks();
});
describe('Main page test', () => {
    it('should call all modules properly', () => {
      const spyTimeHook = jest.spyOn(hooks, 'useCurrentTime').mockReturnValue(
        '00:00:00'
      );
      const spyProductHook = jest.spyOn(hooks, 'useProducts').mockReturnValue(
        [{
          id: 1,
          name: 'IPhone 14 Pro',
          description: 'Latest iphone, buy it now',
          price: 999,
          priceSymbol: '$',
          category: 'Электроника',
          imgUrl: '/iphone.png',
        }]
      );
      const spyApplyUtils = jest.spyOn(utils, 'applyCategories').mockReturnValue(
        [{
          id: 1,
          name: 'IPhone 14 Pro',
          description: 'Latest iphone, buy it now',
          price: 999,
          priceSymbol: '$',
          category: 'Электроника',
          imgUrl: '/iphone.png',
        }]
      ); 
      const spyUpdateUtils = jest.spyOn(utils, 'updateCategories').mockReturnValue(
        ['Одежда']
      );
      const rendered = render(<MainPage />);

      
      expect(spyTimeHook).toHaveBeenCalledTimes(1);
      expect(spyProductHook).toHaveBeenCalledTimes(1);
      expect(spyApplyUtils).toHaveBeenCalledTimes(1);
      fireEvent.click(rendered.getByText('Одежда'));
      expect(spyUpdateUtils).toHaveBeenCalledTimes(1);
      expect(rendered.asFragment()).toMatchSnapshot();
    });
});
