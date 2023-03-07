## ------------------------------------------
## Generated by Transwarp
##
## THIS FILE IS AUTOMATICALLY GENERATED.
## DO NOT EDIT. ALL CHANGES WILL BE LOST.
## ------------------------------------------

import struct
import enum
from dataclasses import dataclass, field
from .amtypes import *
from .megajank import crypto_curse_string, crypto_decurse_string, simple_encrypt_string, simple_decrypt_string

class Type(enum.IntEnum):
    HELLO                     = 0x00 # unknown
    HELLO_ACK                 = 0x01 # unknown
    HELLO_TO                  = 0x02 # unknown
    HELLO_TO_ACK              = 0x03 # unknown
    QUERY_DID                 = 0x08 # unknown
    QUERY_DID_ACK             = 0x09 # unknown
    DEV_LGN                   = 0x10 # unknown
    DEV_LGN_ACK               = 0x11 # unknown
    DEV_LGN_CRC               = 0x12 # unknown
    DEV_LGN_ACK_CRC           = 0x13 # unknown
    DEV_LGN_KEY               = 0x14 # unknown
    DEV_LGN_ACK_KEY           = 0x15 # unknown
    DEV_LGN_DSK               = 0x16 # unknown
    DEV_ONLINE_REQ            = 0x18 # unknown
    DEV_ONLINE_REQ_ACK        = 0x19 # unknown
    P2P_REQ                   = 0x20 # unknown
    P2P_REQ_ACK               = 0x21 # unknown
    P2P_REQ_DSK               = 0x26 # unknown
    LAN_SEARCH                = 0x30 # unknown
    LAN_NOTIFY                = 0x31 # unknown
    LAN_NOTIFY_ACK            = 0x32 # unknown
    PUNCH_TO                  = 0x40 # unknown
    PUNCH_PKT                 = 0x41 # unknown
    PUNCH_PKT_EX              = 0x41 # unknown
    P2P_RDY                   = 0x42 # unknown
    P2P_RDY_EX                = 0x42 # unknown
    P2P_RDY_ACK               = 0x43 # unknown
    RS_LGN                    = 0x60 # unknown
    RS_LGN_ACK                = 0x61 # unknown
    RS_LGN1                   = 0x62 # unknown
    RS_LGN1_ACK               = 0x63 # unknown
    LIST_REQ1                 = 0x67 # unknown
    LIST_REQ                  = 0x68 # unknown
    LIST_REQ_ACK              = 0x69 # unknown
    LIST_REQ_DSK              = 0x6a # unknown
    RLY_HELLO                 = 0x70 # unknown
    RLY_HELLO_ACK             = 0x71 # unknown
    RLY_PORT                  = 0x72 # unknown
    RLY_PORT_ACK              = 0x73 # unknown
    RLY_PORT_KEY              = 0x74 # unknown
    RLY_PORT_ACK_KEY          = 0x75 # unknown
    RLY_BYTE_COUNT            = 0x78 # unknown
    RLY_REQ                   = 0x80 # unknown
    RLY_REQ_ACK               = 0x81 # unknown
    RLY_TO                    = 0x82 # unknown
    RLY_PKT                   = 0x83 # unknown
    RLY_RDY                   = 0x84 # unknown
    RLY_TO_ACK                = 0x85 # unknown
    RLY_SERVER_REQ            = 0x87 # unknown
    RLY_SERVER_REQ_ACK        = 0x87 # unknown
    SDEV_RUN                  = 0x90 # unknown
    SDEV_LGN                  = 0x91 # unknown
    SDEV_LGN_ACK              = 0x91 # unknown
    SDEV_LGN_CRC              = 0x92 # unknown
    SDEV_LGN_ACK_CRC          = 0x92 # unknown
    SDEV_REPORT               = 0x94 # unknown
    CONNECT_REPORT            = 0xa0 # unknown
    REPORT_REQ                = 0xa1 # unknown
    REPORT                    = 0xa2 # unknown
    DRW                       = 0xd0 # unknown
    DRW_ACK                   = 0xd1 # unknown
    PSR                       = 0xd8 # unknown
    ALIVE                     = 0xe0 # unknown
    ALIVE_ACK                 = 0xe1 # unknown
    CLOSE                     = 0xf0 # unknown
    MGM_DUMP_LOGIN_DID        = 0xf4 # unknown
    MGM_DUMP_LOGIN_DID_DETAIL = 0xf5 # unknown
    MGM_DUMP_LOGIN_DID_1      = 0xf6 # unknown
    MGM_LOG_CONTROL           = 0xf7 # unknown
    MGM_REMOTE_MANAGEMENT     = 0xf8 # unknown
    REPORT_SESSION_READY      = 0xf9 # unknown
    INVALID                   = 0xff # unknown

    @classmethod
    def parse(cls, p):
        return cls(struct.unpack("B", p[:1])[0]), p[1:]

@dataclass
class Host:
    pad0 : bytes = field(repr=False) # unknown
    afam : u8le # Adress family. Set to AF_INET (2)
    port : u16le # Port number
    addr : IPv4 # IP address
    pad1 : bytes = field(repr=False) # unknown

    @classmethod
    def parse(cls, p):
        pad0, p = Zeroes.parse(p, 1)
        afam, p = u8le.parse(p)
        port, p = u16le.parse(p)
        addr, p = IPv4.parse(p)
        pad1, p = Zeroes.parse(p, 8)
        return cls(pad0, afam, port, addr, pad1), p

    def pack(self):
        p  = Zeroes.pack(self.pad0, 1)
        p += self.afam.pack()
        p += self.port.pack()
        p += self.addr.pack()
        p += Zeroes.pack(self.pad1, 8)
        return p

@dataclass
class Duid:
    prefix : bytes # duid "prefix", 7 chars + NULL terminator
    serial : u32 # device serial number
    check  : bytes # checkcode relating to prefix+serial
    pad0   : bytes = field(repr=False) # padding

    @classmethod
    def parse(cls, p):
        prefix, p = String.parse(p, 8)
        serial, p = u32.parse(p)
        check, p = String.parse(p, 6)
        pad0, p = Zeroes.parse(p, 2)
        return cls(prefix, serial, check, pad0), p

    def pack(self):
        p  = String.pack(self.prefix, 8)
        p += self.serial.pack()
        p += String.pack(self.check, 6)
        p += Zeroes.pack(self.pad0, 2)
        return p

@dataclass
class Xzyh:
    magic : bytes # unknown

    @classmethod
    def parse(cls, p):
        magic, p = bytes.parse(p, 4)
        return cls(magic), p

    def pack(self):
        p  = self.magic.pack()
        return p

@dataclass
class Aabb:
    magic : u16 # Signature bytes. Must be 0xAABB
    unk   : u16 # Unknown field
    cmd   : u32 # Command field (unknown function)
    len   : u32 # Length field

    @classmethod
    def parse(cls, p):
        magic, p = u16.parse(p)
        unk, p = u16.parse(p)
        cmd, p = u32.parse(p)
        len, p = u32.parse(p)
        return cls(magic, unk, cmd, len), p

    def pack(self):
        p  = self.magic.pack()
        p += self.unk.pack()
        p += self.cmd.pack()
        p += self.len.pack()
        return p

@dataclass
class Dsk:
    key : bytes # unknown

    @classmethod
    def parse(cls, p):
        key, p = bytes.parse(p, 24)
        return cls(key), p

    def pack(self):
        p  = self.key.pack()
        return p

@dataclass
class Version:
    major : u8 # unknown
    minor : u8 # unknown
    patch : u8 # unknown

    @classmethod
    def parse(cls, p):
        major, p = u8.parse(p)
        minor, p = u8.parse(p)
        patch, p = u8.parse(p)
        return cls(major, minor, patch), p

    def pack(self):
        p  = self.major.pack()
        p += self.minor.pack()
        p += self.patch.pack()
        return p

@dataclass
class PktDrw:
    magic : u8 # Signature byte. Must be 0xD1
    chan  : u8 # Channel index
    index : u16 # Packet index

    @classmethod
    def parse(cls, p):
        magic, p = u8.parse(p)
        chan, p = u8.parse(p)
        index, p = u16.parse(p)
        return cls(magic, chan, index), p

    def pack(self):
        p  = self.magic.pack()
        p += self.chan.pack()
        p += self.index.pack()
        return p

@dataclass
class PktDrwAck:
    magic : u8 # Signature byte. Must be 0xD1
    chan  : u8 # Channel index
    count : u16 # Number of acks following
    acks  : list[u16] # Array of acknowledged DRW packet

    @classmethod
    def parse(cls, p):
        magic, p = u8.parse(p)
        chan, p = u8.parse(p)
        count, p = u16.parse(p)
        acks, p = Array.parse(p, u16, count)
        return cls(magic, chan, count, acks), p

    def pack(self):
        p  = self.magic.pack()
        p += self.chan.pack()
        p += self.count.pack()
        p += Array.pack(self.acks, u16)
        return p

@dataclass
class PktPunchTo:
    host : Host # unknown

    @classmethod
    def parse(cls, p):
        host, p = Host.parse(p)
        return cls(host), p

    def pack(self):
        p  = self.host.pack()
        return p

@dataclass
class PktHello:

    @classmethod
    def parse(cls, p):
        return cls(), p

    def pack(self):
        p = b""
        return p

@dataclass
class PktLanSearch:

    @classmethod
    def parse(cls, p):
        return cls(), p

    def pack(self):
        p = b""
        return p

@dataclass
class PktRlyHello:

    @classmethod
    def parse(cls, p):
        return cls(), p

    def pack(self):
        p = b""
        return p

@dataclass
class PktAlive:

    @classmethod
    def parse(cls, p):
        return cls(), p

    def pack(self):
        p = b""
        return p

@dataclass
class PktAliveAck:

    @classmethod
    def parse(cls, p):
        return cls(), p

    def pack(self):
        p = b""
        return p

@dataclass
class PktClose:

    @classmethod
    def parse(cls, p):
        return cls(), p

    def pack(self):
        p = b""
        return p

@dataclass
class PktHelloAck:
    host : Host # unknown

    @classmethod
    def parse(cls, p):
        host, p = Host.parse(p)
        return cls(host), p

    def pack(self):
        p  = self.host.pack()
        return p

@dataclass
class PktPunchPkt:
    duid : Duid # unknown

    @classmethod
    def parse(cls, p):
        duid, p = Duid.parse(p)
        return cls(duid), p

    def pack(self):
        p  = self.duid.pack()
        return p

@dataclass
class PktP2pRdy:
    duid : Duid # unknown

    @classmethod
    def parse(cls, p):
        duid, p = Duid.parse(p)
        return cls(duid), p

    def pack(self):
        p  = self.duid.pack()
        return p

@dataclass
class PktP2pReq:
    duid : Duid # unknown
    host : Host # unknown

    @classmethod
    def parse(cls, p):
        duid, p = Duid.parse(p)
        host, p = Host.parse(p)
        return cls(duid, host), p

    def pack(self):
        p  = self.duid.pack()
        p += self.host.pack()
        return p

@dataclass
class PktP2pReqAck:

    @classmethod
    def parse(cls, p):
        return cls(), p

    def pack(self):
        p = b""
        return p

@dataclass
class PktP2pReqDsk:
    duid     : Duid # unknown
    host     : Host # unknown
    nat_type : u8 # unknown
    version  : Version # unknown
    dsk      : Dsk # unknown

    @classmethod
    def parse(cls, p):
        duid, p = Duid.parse(p)
        host, p = Host.parse(p)
        nat_type, p = u8.parse(p)
        version, p = Version.parse(p)
        dsk, p = Dsk.parse(p)
        return cls(duid, host, nat_type, version, dsk), p

    def pack(self):
        p  = self.duid.pack()
        p += self.host.pack()
        p += self.nat_type.pack()
        p += self.version.pack()
        p += self.dsk.pack()
        return p

@dataclass
class PktP2pRdyAck:
    duid : Duid # unknown
    host : Host # unknown
    pad  : bytes = field(repr=False) # unknown

    @classmethod
    def parse(cls, p):
        duid, p = Duid.parse(p)
        host, p = Host.parse(p)
        pad, p = Zeroes.parse(p, 8)
        return cls(duid, host, pad), p

    def pack(self):
        p  = self.duid.pack()
        p += self.host.pack()
        p += Zeroes.pack(self.pad, 8)
        return p

@dataclass
class PktListReqDsk:
    duid : Duid # Device id
    dsk  : Dsk # Device secret key

    @classmethod
    def parse(cls, p):
        duid, p = Duid.parse(p)
        dsk, p = Dsk.parse(p)
        return cls(duid, dsk), p

    def pack(self):
        p  = self.duid.pack()
        p += self.dsk.pack()
        return p

@dataclass
class PktListReqAck:
    numr   : u8 # Number of relays
    pad    : bytes = field(repr=False) # Padding
    relays : list[Host] # Available relay hosts

    @classmethod
    def parse(cls, p):
        numr, p = u8.parse(p)
        pad, p = Zeroes.parse(p, 3)
        relays, p = Array.parse(p, Host, numr)
        return cls(numr, pad, relays), p

    def pack(self):
        p  = self.numr.pack()
        p += Zeroes.pack(self.pad, 3)
        p += Array.pack(self.relays, Host)
        return p

@dataclass
class PktDevLgnCrc:
    duid     : Duid # unknown
    nat_type : u8 # unknown
    version  : Version # unknown
    host     : Host # unknown

    @classmethod
    def parse(cls, p):
        p = crypto_decurse_string(p)
        duid, p = Duid.parse(p)
        nat_type, p = u8.parse(p)
        version, p = Version.parse(p)
        host, p = Host.parse(p)
        return cls(duid, nat_type, version, host), p

    def pack(self):
        p  = self.duid.pack()
        p += self.nat_type.pack()
        p += self.version.pack()
        p += self.host.pack()
        return crypto_curse_string(p)

@dataclass
class PktRlyTo:
    host : Host # unknown
    mark : u32 # unknown

    @classmethod
    def parse(cls, p):
        host, p = Host.parse(p)
        mark, p = u32.parse(p)
        return cls(host, mark), p

    def pack(self):
        p  = self.host.pack()
        p += self.mark.pack()
        return p

@dataclass
class PktRlyPkt:
    mark : u32 # unknown
    duid : Duid # unknown

    @classmethod
    def parse(cls, p):
        mark, p = u32.parse(p)
        duid, p = Duid.parse(p)
        return cls(mark, duid), p

    def pack(self):
        p  = self.mark.pack()
        p += self.duid.pack()
        return p

@dataclass
class PktRlyRdy:
    duid : Duid # unknown

    @classmethod
    def parse(cls, p):
        duid, p = Duid.parse(p)
        return cls(duid), p

    def pack(self):
        p  = self.duid.pack()
        return p

@dataclass
class PktDevLgnAckCrc:
    pad0 : bytes = field(repr=False) # unknown

    @classmethod
    def parse(cls, p):
        p = crypto_decurse_string(p)
        pad0, p = Zeroes.parse(p, 4)
        return cls(pad0), p

    def pack(self):
        p  = Zeroes.pack(self.pad0, 4)
        return crypto_curse_string(p)

@dataclass
class PktSessionReady:
    duid           : Duid # unknown
    handle         : i32 # unknown
    max_handles    : u16 # unknown
    active_handles : u16 # unknown
    startup_ticks  : u16 # unknown
    b1             : u8 # unknown
    b2             : u8 # unknown
    b3             : u8 # unknown
    b4             : u8 # unknown
    pad0           : bytes = field(repr=False) # unknown
    addr_local     : Host # unknown
    addr_wan       : Host # unknown
    addr_relay     : Host # unknown

    @classmethod
    def parse(cls, p):
        p = simple_decrypt_string(p)
        duid, p = Duid.parse(p)
        handle, p = i32.parse(p)
        max_handles, p = u16.parse(p)
        active_handles, p = u16.parse(p)
        startup_ticks, p = u16.parse(p)
        b1, p = u8.parse(p)
        b2, p = u8.parse(p)
        b3, p = u8.parse(p)
        b4, p = u8.parse(p)
        pad0, p = Zeroes.parse(p, 2)
        addr_local, p = Host.parse(p)
        addr_wan, p = Host.parse(p)
        addr_relay, p = Host.parse(p)
        return cls(duid, handle, max_handles, active_handles, startup_ticks, b1, b2, b3, b4, pad0, addr_local, addr_wan, addr_relay), p

    def pack(self):
        p  = self.duid.pack()
        p += self.handle.pack()
        p += self.max_handles.pack()
        p += self.active_handles.pack()
        p += self.startup_ticks.pack()
        p += self.b1.pack()
        p += self.b2.pack()
        p += self.b3.pack()
        p += self.b4.pack()
        p += Zeroes.pack(self.pad0, 2)
        p += self.addr_local.pack()
        p += self.addr_wan.pack()
        p += self.addr_relay.pack()
        return simple_encrypt_string(p)


MessageTypeTable = {
    Type.HELLO                : PktHello,
    Type.HELLO_ACK            : PktHelloAck,
    Type.DEV_LGN_CRC          : PktDevLgnCrc,
    Type.DEV_LGN_ACK_CRC      : PktDevLgnAckCrc,
    Type.P2P_REQ              : PktP2pReq,
    Type.P2P_REQ_ACK          : PktP2pReqAck,
    Type.P2P_REQ_DSK          : PktP2pReqDsk,
    Type.LAN_SEARCH           : PktLanSearch,
    Type.PUNCH_TO             : PktPunchTo,
    Type.PUNCH_PKT            : PktPunchPkt,
    Type.P2P_RDY              : PktP2pRdy,
    Type.P2P_RDY_ACK          : PktP2pRdyAck,
    Type.LIST_REQ_ACK         : PktListReqAck,
    Type.LIST_REQ_DSK         : PktListReqDsk,
    Type.RLY_HELLO            : PktRlyHello,
    Type.RLY_TO               : PktRlyTo,
    Type.RLY_PKT              : PktRlyPkt,
    Type.RLY_RDY              : PktRlyRdy,
    Type.DRW                  : PktDrw,
    Type.DRW_ACK              : PktDrwAck,
    Type.ALIVE                : PktAlive,
    Type.ALIVE_ACK            : PktAliveAck,
    Type.CLOSE                : PktClose,
    Type.REPORT_SESSION_READY : PktSessionReady,
}

MessageTypeRevTable = {
    "PktHello": Type.HELLO,
    "PktHelloAck": Type.HELLO_ACK,
    "PktDevLgnCrc": Type.DEV_LGN_CRC,
    "PktDevLgnAckCrc": Type.DEV_LGN_ACK_CRC,
    "PktP2pReq": Type.P2P_REQ,
    "PktP2pReqAck": Type.P2P_REQ_ACK,
    "PktP2pReqDsk": Type.P2P_REQ_DSK,
    "PktLanSearch": Type.LAN_SEARCH,
    "PktPunchTo": Type.PUNCH_TO,
    "PktPunchPkt": Type.PUNCH_PKT,
    "PktP2pRdy": Type.P2P_RDY,
    "PktP2pRdyAck": Type.P2P_RDY_ACK,
    "PktListReqAck": Type.LIST_REQ_ACK,
    "PktListReqDsk": Type.LIST_REQ_DSK,
    "PktRlyHello": Type.RLY_HELLO,
    "PktRlyTo": Type.RLY_TO,
    "PktRlyPkt": Type.RLY_PKT,
    "PktRlyRdy": Type.RLY_RDY,
    "PktDrw": Type.DRW,
    "PktDrwAck": Type.DRW_ACK,
    "PktAlive": Type.ALIVE,
    "PktAliveAck": Type.ALIVE_ACK,
    "PktClose": Type.CLOSE,
    "PktSessionReady": Type.REPORT_SESSION_READY,
}

class Message:

    @classmethod
    def parse(cls, m):
        magic, typ, size = struct.unpack(">BBH", m[:4])
        assert magic == 0xF1
        typ = Type(typ)
        p = m[4:4+size]
        if typ in MessageTypeTable:
            return MessageTypeTable[typ].parse(p)
        else:
            raise ValueError(f"unknown message type {typ:02x}")

    @staticmethod
    def pack(pkt):
        name = type(pkt).__name__
        if not name in MessageTypeRevTable:
            raise ValueError(f"unknown message type {type(pkt)}")
        p = pkt.pack()
        return struct.pack(">BBH", 0xF1, MessageTypeRevTable[name], len(p)) + p