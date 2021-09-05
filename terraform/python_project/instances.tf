data "aws_ami" "ubuntu_20" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  owners = ["099720109477"] # Canonical
}

resource "aws_instance" "clock" {
  count                       = 1
  ami                         = data.aws_ami.ubuntu_20.id
  instance_type               = "t2.micro"
  vpc_security_group_ids      = [aws_security_group.clock_server_sg.id]
  subnet_id                   = aws_subnet.deploy.id
  associate_public_ip_address = true
  key_name = "deployer-key"

  tags = {
    Name = "Clock server"
  }
}