DROP TABLE IF EXISTS data;

CREATE TABLE data (
  product_name VARCHAR (50) NOT NULL,
  price VARCHAR (20),
  stock VARCHAR (20),
  url VARCHAR (150),
  company VARCHAR (30)
  p_type VARCHAR (30)
  img_url VARCHAR (150)
  FOREIGN KEY (data_id) REFERENCES (data_id)
);

