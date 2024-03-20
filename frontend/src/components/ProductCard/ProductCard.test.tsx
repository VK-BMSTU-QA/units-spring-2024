import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';

afterEach(jest.clearAllMocks);
describe('Product card test', () => {
    it('should render correctly', () => {
        const rendered = render(<ProductCard
            id={1}
            name={'Pinspire'}
            description={'by OND team'}
            price={999999}
            priceSymbol={'$'}
            category={'Для дома'}
            imgUrl={'https://pinspire.site/pin/feed'}
        />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    it('should add class for selected', () => {
        const rendered = render(<ProductCard
            id={1}
            name={'Pinspire'}
            description={'by OND team'}
            price={999999}
            priceSymbol={'$'}
            category={'Для дома'}
            imgUrl={'https://pinspire.site/pin/feed'}
        />);

        expect(rendered.getByText('Pinspire')).toHaveClass(
            'product-card__name'
        );
        expect(rendered.getByText('by OND team')).not.toHaveClass(
            'product-card__name'
        );
        expect(rendered.getByText('Для дома')).not.toHaveClass(
            'product-card'
        );
    });
});
