import { applyCategories } from '../applyCategories';
import type { Product, Category } from '../../types';

describe('applyCategories', () => {
    const products:  Product[] = [
      {
        id: 1,
        name: 'Телефон',
        description: 'Описание продукта 1',
        price: 100,
        category: 'Электроника'
      },
      {
        id: 2,
        name: 'Швабра',
        description: 'Описание продукта 2',
        price: 200,
        category: 'Для дома'
      },
      {
        id: 3,
        name: 'Штаны',
        description: 'Описание продукта 3',
        price: 150,
        category: 'Одежда'
      },
      {
        id: 4,
        name: 'Ноутбук',
        description: 'Описание продукта 4',
        price: 100,
        category: 'Электроника'
      },
      {
        id: 5,
        name: 'Мыло',
        description: 'Описание продукта 5',
        price: 200,
        category: 'Для дома'
      },
      {
        id: 6,
        name: 'Футболка',
        description: 'Описание продукта 6',
        price: 150,
        category: 'Одежда'
      }
    ];
  
    const categories:  Category[] = ['Электроника'];
  
    it('should return products with specified categories', () => {
      expect(applyCategories(products, categories)).toEqual([
        {
          id: 1,
          name: 'Телефон',
          description: 'Описание продукта 1',
          price: 100,
          category: 'Электроника'
        },
        {
          id: 4,
          name: 'Ноутбук',
          description: 'Описание продукта 4',
          price: 100,
          category: 'Электроника'
        }
      ]);

      expect(applyCategories(products, ['Одежда'])).toEqual([
        {
          id: 3,
          name: 'Штаны',
          description: 'Описание продукта 3',
          price: 150,
          category: 'Одежда'
        },
        {
          id: 6,
          name: 'Футболка',
          description: 'Описание продукта 6',
          price: 150,
          category: 'Одежда'
        }
      ]);

      expect(applyCategories(products, ['Для дома'])).toEqual([
        {
          id: 2,
          name: 'Швабра',
          description: 'Описание продукта 2',
          price: 200,
          category: 'Для дома'
        },
        {
          id: 5,
          name: 'Мыло',
          description: 'Описание продукта 5',
          price: 200,
          category: 'Для дома'
        }
      ]);
    });
  
    it('should return all products if no categories are specified', () => {
      expect(applyCategories(products, [])).toEqual(products);
    });
  
    it('should return empty array if no products are provided', () => {
      expect(applyCategories([], categories)).toEqual([]);
    });
  });