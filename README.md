# MAC Changer 🖧🛠

This is a simple Python script that allows you to change the MAC address of a network interface on Linux systems.

## 🧠 What is a MAC Address?

A MAC (Media Access Control) address is a unique identifier assigned to network interfaces. Changing it can help with:
- Privacy protection
- Network testing
- Bypassing MAC-based filters

## 🚀 Features

- Change MAC address using command-line arguments
- Verifies MAC address before and after changing
- Easy to use with `-i` for interface and `-m` for new MAC

## 🛠 Requirements

- Linux system
- Python 3
- `ifconfig` command (usually comes with `net-tools` package)

## 📦 Installation

```bash
sudo apt install net-tools
