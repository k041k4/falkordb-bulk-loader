# from falkordb_bulk_loader import bulk_insert
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("debug.log"), logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

def insert_taxonomy():
    logger.info("Starting taxonomy insertion")
    # bulk_insert.bulk_insert(
    #     graph="Ecosided",

    #     server_url="http://r-6jissuruar.instance-ke10zfyqz.hc-mjfsf95pz.us-west-2.aws.f2e0a955bb84.cloud:58718",
    #     nodes=["./taxonomy.csv"],
    #     nodes_with_label=["taxonomy_with_label.csv"],
    #     relations=["taxonomy_relations.csv"],
    #     relations_with_type=["taxonomy_relations_with_type.csv"],
    #     separator=",",
    #     enforce_schema=True,
    #     id_type="uuid",
    #     skip_invalid_nodes=False,
    #     skip_invalid_edges=False,
    #     escapechar="\\",
    #     quote=0,
    #     max_token_count=1024,
    #     max_buffer_size=64,
    #     max_token_size=64,
    # )

if __name__ == "__main__":
    insert_taxonomy()
