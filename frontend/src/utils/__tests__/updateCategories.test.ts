import { updateCategories } from '../updateCategories';

describe('test update categories function', () => {
    it('should return category massive without changedCategories value', () => {
        expect(
            updateCategories(['Для дома', 'Электроника'], 'Электроника')
        ).toEqual(['Для дома']);
    });
    it('should return category massive with changedCategories value', () => {
        expect(updateCategories(['Для дома', 'Электроника'], 'Одежда')).toEqual(
            ['Для дома', 'Электроника', 'Одежда']
        );
    });
});

