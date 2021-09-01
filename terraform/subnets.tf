# Networking setup to make instance available for external world
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/24"
}

resource "aws_internet_gateway" "igw" {
  vpc_id = aws_vpc.main.id
}

resource "aws_default_route_table" "main_route_table" {
  default_route_table_id = aws_vpc.main.default_route_table_id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.igw.id
  }
}

resource "aws_subnet" "deploy" {
  vpc_id     = aws_vpc.main.id
  cidr_block = aws_vpc.main.cidr_block
}