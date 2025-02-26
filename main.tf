terraform {
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "6.22.0"
    }
  }
}

provider "google" {
  project = "your-gcp-project-id"
  region  = "us-central1"
}

resource "google_compute_instance" "vm_instance" {
  name         = "terraform-vm"
  machine_type = "e2-medium"
  zone         = "us-central1-a"

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = "default"

    access_config {
      // Assigns an external IP
    }
  }

  metadata_startup_script = <<-EOT
    #!/bin/bash
    echo "Hello, Terraform!" > /var/tmp/hello.txt
  EOT

  tags = ["web"]

}

resource "google_compute_firewall" "default" {
  name    = "allow-ssh"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["22"]
  }

  source_ranges = ["0.0.0.0/0"]
  target_tags   = ["web"]
}
