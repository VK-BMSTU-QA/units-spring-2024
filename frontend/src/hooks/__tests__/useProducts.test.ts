import { renderHook } from '@testing-library/react-hooks';
import { useProducts } from '../useProducts';

describe('useProducts', () => {
  it('returns an array of products', () => {
    const { result } = renderHook(() => useProducts());

    expect(result.current).toHaveLength(4);
    expect(result.current[0]).toEqual({
      id: 1,
      name: 'IPhone 14 Pro',
      description: 'Latest iphone, buy it now',
      price: 999,
      priceSymbol: '$',
      category: 'Электроника',
      imgUrl: '/iphone.png',
    });
  });
});