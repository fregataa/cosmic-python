import model
import repository


def test_repository_can_save_a_batch(session):
    batch = model.Batch("batch1", "OLD-COUCH", 100, eta=None)

    repo = repository.SqlAlchemyRepository(session)
    # repo.add is tested in this test.
    repo.add(batch)
    session.commit()

    rows = session.execute(
        'SELECT reference, sku, _purchased_quantity, eta FROM "batches"'
    )
    assert list(rows) == [("batch1", "OLD-COUCH", 100, None)]
