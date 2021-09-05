variable "deploy_pubkey_path" {
  type        = string
  description = "Public key file, that will be known for deployed instances"
  default     = "~/.ssh/aws.pub"
}
